fetch('./data/current.json').then(r=>r.ok?r.json():{}).then(d=>{document.querySelector('#trajectory').textContent=d.trajectory||'insufficient_data'}).catch(()=>{});
