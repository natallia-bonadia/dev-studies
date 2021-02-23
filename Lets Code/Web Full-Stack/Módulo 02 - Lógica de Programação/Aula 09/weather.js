const { default: Axios } = require('axios')
const axios = require('axios')

const apiKey = '5d0b33a3adaa365fb1561a27d2baade8'

async function getData(city = 'Paris'){
  let url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=pt_br`

  const response = await axios.get(url)
  const {main, weather: [info]} = response.data
  const text = `
Cidade: ${city}
Descrição: ${info.description}
Temperatura: ${main.temp} °C
Mín: ${main.temp_min} °C
Máx: ${main.temp_max} °C
`
console.log(text)
}

getData()

// console.log('Texto depois da chamada da funcao')


async function randomuser(){
  let url = 'https://randomuser.me/api/'
  const response = await axios.get(url)
  const {results: [infos]} = response.data
const text = `
Nome: ${infos.name.first} ${infos.name.last}
País: ${infos.location.country} 
Estado: ${infos.location.state}
Cidade: ${infos.location.city}
Telefone: ${infos.phone}
Celular: ${infos.cell}
`
console.log(text)
}

randomuser()