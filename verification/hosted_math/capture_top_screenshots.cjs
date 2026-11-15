'use strict';
// Supplementary visual evidence; the canonical mathematical comparison is separate.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {chromium}=require('playwright');
const {waitForHostedMath}=require('./capture_hosted_math.cjs');
const sha256=b=>crypto.createHash('sha256').update(b).digest('hex');
(async()=>{
  const [input,output]=process.argv.slice(2);
  if(!input || !output) throw new Error('Use INPUT_CAPTURE_DIRECTORY EMPTY_OUTPUT_DIRECTORY');
  const report=JSON.parse(fs.readFileSync(path.join(input,'hosted-report.json')));
  const source=JSON.parse(fs.readFileSync(path.join(input,'math-source.json')));
  if(report.status!=='pass' || source.revision!==report.revision) throw new Error('A passing bound mathematical capture is required');
  if(fs.existsSync(output) && fs.readdirSync(output).length) throw new Error('Use an empty output directory');
  fs.mkdirSync(output,{recursive:true});
  const browser=await chromium.launch({headless:true});
  const observations=[];
  try{
    for(const width of [1440,760]){
      const context=await browser.newContext({viewport:{width,height:1000},deviceScaleFactor:1,colorScheme:'light'});
      try{
        for(const [index,item] of source.pages.entries()){
          const page=await context.newPage();
          try{
            const response=await page.goto(item.url,{waitUntil:'domcontentloaded',timeout:60000});
            if(response.status()!==200 || page.url()!==item.url) throw new Error('Exact source URL unavailable');
            const article=page.locator('article.markdown-body').first();
            await article.waitFor({state:'visible',timeout:30000});
            await page.evaluate(async()=>{
              for(let y=0,n=0;y<document.body.scrollHeight && n<200;y+=900,n++){
                window.scrollTo(0,y);await new Promise(r=>setTimeout(r,50));
              }
              window.scrollTo(0,0);
            });
            await waitForHostedMath(article,item.expressions.length);
            await page.evaluate(async()=>{
              window.scrollTo(0,0);
              await new Promise(r=>setTimeout(r,750));
              await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
            });
            if(await page.evaluate(()=>window.scrollY)!==0) throw new Error('Page did not settle at the top');
            const name=String(index+1).padStart(4,'0')+'-'+width+'.png';
            await page.screenshot({path:path.join(output,name),fullPage:true,timeout:30000});
            const bytes=fs.readFileSync(path.join(output,name));
            observations.push({path:item.path,source_sha256:item.source_sha256,width,scroll_y:0,
              screenshot:name,size_bytes:bytes.length,sha256:sha256(bytes),observed_at:new Date().toISOString()});
          }finally{await page.close();}
        }
      }finally{await context.close();}
    }
  }finally{await browser.close();}
  fs.writeFileSync(path.join(output,'visual-report.json'),JSON.stringify({schema_version:1,
    kind:'hosted_visual_supplement',repository:report.repository,revision:report.revision,tree:report.tree,
    mathematical_report_sha256:sha256(fs.readFileSync(path.join(input,'hosted-report.json'))),
    observations,limits:'Additional actual-host screenshots after settled top scrolling; requires visual inspection and does not replace the mathematical structural report.'},null,2)+'\n');
  process.stdout.write(JSON.stringify({screenshots:observations.length,output})+'\n');
})().catch(e=>{process.stderr.write(String(e)+'\n');process.exitCode=1;});
