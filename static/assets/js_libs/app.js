const options = {
    margin: 0.5,
    filename: 'invoice.pdf',    //name the output file
    image: { 
      type: 'jpeg',     //image type
      quality: 100
    },
    html2canvas: { 
      scale: 1 
    },
    jsPDF: { 
      unit: 'in', 
      format: 'letter', 
      orientation: 'portrait'   // pdf orientation
    }
  }


const area_pdf=document.getElementsByClassName('main-body');
         const btn=document.getElementById('qc-btn');
         btn.addEventListener('click',()=>{
                console.log('hello');

            html2pdf().from(area_pdf).set(options).save();
         }) ; 





