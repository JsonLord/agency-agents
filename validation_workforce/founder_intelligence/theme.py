from pathlib import Path
def derive(design,output,name='company'):
 text=Path(design).read_text(); out=Path(output);out.mkdir(parents=True,exist_ok=True)
 (out/f'{name}.md').write_text('# Theme: '+name+'\n\nDerived from DESIGN.md\n\n'+text)
 (out/f'{name}.demo.tsx').write_text("export const themeSource = 'DESIGN.md';\nexport default function Demo(){return <main><h1>Company theme</h1></main>}\n")
 return [out/f'{name}.md',out/f'{name}.demo.tsx']
