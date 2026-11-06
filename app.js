const box=document.querySelector('#lightbox');document.querySelectorAll('[data-image]').forEach(button=>button.addEventListener('click',()=>{box.querySelector('img').src=button.dataset.image;box.showModal()}));box.querySelector('.close').addEventListener('click',()=>box.close());box.addEventListener('click',event=>{if(event.target===box)box.close()});
const stories=document.querySelector('.stories');
if(stories){
 const slides=[...stories.querySelectorAll('.portal-slide')],dots=[...stories.querySelectorAll('.story-dot')],pause=stories.querySelector('.story-pause');
 let current=0,timer,paused=false,start=null,suppressClick=false;
 const schedule=()=>{clearTimeout(timer);if(slides.length>1&&!paused&&!document.hidden)timer=setTimeout(()=>show(current+1),5000)};
 const show=index=>{current=(index+slides.length)%slides.length;slides.forEach((s,i)=>s.hidden=i!==current);dots.forEach((d,i)=>d.setAttribute('aria-pressed',String(i===current)));schedule()};
 dots.forEach((d,i)=>d.addEventListener('click',()=>show(i)));
 pause?.addEventListener('click',()=>{paused=!paused;pause.textContent=paused?'▶':'Ⅱ';pause.setAttribute('aria-label',paused?'Retomar troca automática':'Pausar troca automática');schedule()});
 stories.addEventListener('pointerdown',event=>{if(event.button!==0||event.target.closest('button'))return;start={x:event.clientX,y:event.clientY,id:event.pointerId};clearTimeout(timer);suppressClick=false;stories.classList.add('dragging')});
 window.addEventListener('pointerup',event=>{if(!start||event.pointerId!==start.id)return;const dx=event.clientX-start.x,dy=event.clientY-start.y;start=null;stories.classList.remove('dragging');if(Math.abs(dx)>45&&Math.abs(dx)>Math.abs(dy)){suppressClick=true;show(current+(dx<0?1:-1));setTimeout(()=>suppressClick=false,300)}else schedule()});
 window.addEventListener('pointercancel',()=>{start=null;stories.classList.remove('dragging');schedule()});
 stories.addEventListener('click',event=>{if(suppressClick){event.preventDefault();event.stopPropagation()}},true);
 stories.addEventListener('dragstart',event=>event.preventDefault());
 stories.addEventListener('keydown',event=>{if(event.key==='ArrowRight'||event.key==='ArrowLeft'){event.preventDefault();show(current+(event.key==='ArrowRight'?1:-1))}});
 document.addEventListener('visibilitychange',schedule);schedule();
}
