console.log('Hello World Evaluation')


//*** --- CHOICES --- ***//
let choices = [...document.getElementsByClassName('choice')];
// Tous les labels qui se trouvent dans les classes option
choices.forEach(labels => {
  let choiceLabels = [...labels.getElementsByTagName('label')]
  // Tous les inputs qui se trouvent dans les labels inclus dans des classes eval
  choiceLabels.forEach(label => {
    let choiceInput = label.getElementsByTagName('input')
    if (choiceInput[0].value){
      if (choiceInput[0].value == "1" || choiceInput[0].value == "2" || choiceInput[0].value == "3"){
        label.innerHTML = `<input type="${choiceInput[0].type}" name="${choiceInput[0].name}"
                                  value="${choiceInput[0].value}" id="${choiceInput[0].id}">
                                  <span></span>
                              `
     }  else {
          label.innerHTML = `<input type="${choiceInput[0].type}" name="${choiceInput[0].name}"
                                  value="${choiceInput[0].value}" id="${choiceInput[0].id}">
                                  <span>${choiceInput[0].value}</span>
                                  `
        }
    } else {
      label.innerHTML = ''
      }
  })
})

//*** --- DATES --- ***//
dates = [...document.getElementsByClassName('date')];
dates.forEach(date => {
  let dateLabel = [...date.getElementsByTagName('label')]
  let dateInput = date.getElementsByTagName('input')
  let dateI = date.getElementsByTagName('i')
  console.log(dateLabel)
  dateLabel[0].innerHTML = ''
  dateInput[0].type = 'text'
  dateI[0].innerHTML = ''
})
$(document).ready(function(){
    $('.datepicker').datepicker({'format': 'yyyy-mm-dd'});
  });


//*** --- Quiz display--- ***//
actives = document.querySelectorAll('.active');

actives.forEach(function(item, index){
  if (index == 0 ) {
    let next = item.querySelector('.next');
    let previous = item.querySelector('.back');
    previous.classList.add('noVisible')
    next.addEventListener('click', () => {
      actives[index].classList.remove('visible');
      actives[index + 1].classList.add('visible');
    })
  }
  if ((index > 0) && (index < actives.length - 1)) {
    let previous = item.querySelector('.back');
    let next = item.querySelector('.next');
    previous.addEventListener('click', () => {
      actives[index].classList.remove('visible');
      actives[index - 1].classList.add('visible');
    })
    next.addEventListener('click', () => {
      actives[index].classList.remove('visible');
      actives[index + 1].classList.add('visible');
    })
  }
  if (index == actives.length - 1) {
    let previous = item.querySelector('.back');
    let next = item.querySelector('.next');
    previous.addEventListener('click', () => {
      actives[index].classList.remove('visible');
      actives[index - 1].classList.add('visible');
    })
  }
})






