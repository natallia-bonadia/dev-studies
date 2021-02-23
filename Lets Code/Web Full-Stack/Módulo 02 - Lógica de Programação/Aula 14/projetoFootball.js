const axios = require('axios')
const input = require('readline-sync')

async function main(){
  let country = await getCountry()
  const getText = (partialText, team) => partialText + `--------------------\nTime: ${team.name}\nAno: ${team.year}\nEstádio: ${team.stadium}\nLocalização: ${team.location}\nCapacidade: ${team.capacity}\n`
  let text = country.reduce(getText, '\n')
  let option
  const menu = `
Escolha uma das opcoes abaixo:
[ 1 ] Filtrar por ano
[ 2 ] Filtrar por capacidade
[ 3 ] Capacidade total
[ 4 ] Obter detalhes de um time
[ 5 ] Nova busca
[ 0 ] Sair do programa
`
console.log(text)

  do {
    option = input.question(`${menu} >>> `)
    if (option == 1){
      let year = parseInt(input.question('Times com ano de inauguracao acima de: '))
      country = country.filter(team => team.year > year)
      text = country.reduce(getText, '\n')
      console.log(text)
    }
    else if (option == 2){
      let capacity = parseInt(input.question('Times com capacidade acima de: '))
      country = country.filter(team => team.capacity > capacity)
      text = country.reduce(getText, '\n')
      console.log(text)
    }
    else if (option == 3){
      const totalCapacity = country.reduce((partialCap, team) => partialCap + team.capacity, 0)
      console.log(`Capacidade total dos estadios: ${totalCapacity}`)
    }
    else if (option == 4){
      let search = input.question('Digite o time: ')
      let team = search[0].toUpperCase() + search.substr(1)
      let url = await axios.get(`https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=${team}`)
                                .then(res => res.data)
                                .then(data => data.teams)
                                .then(teams => teams.map(
                                  team => ({description: team.strDescriptionEN})))
      text = url.reduce((partialText, team) => partialText + `Descricao: ${team.description}`, '\n')
      console.log(text)
    }
    else if (option == 5) {
      country = await getCountry()
      let text = country.reduce(getText, '\n')
      let option
      const menu = `
    Escolha uma das opcoes abaixo:
    [ 1 ] Filtrar por ano
    [ 2 ] Filtrar por capacidade
    [ 3 ] Capacidade total
    [ 4 ] Obter detalhes de um time
    [ 5 ] Nova busca
    [ 0 ] Sair do programa
    `
    console.log(text)
    }
  } while (option != 0){
    console.log('Programa finalizado.')
  }
}

async function getCountry(){
  console.log(`\n--------------------
  Times de Futebol
--------------------`)
  let search = input.question('Digite o pais para pesquisar: ')
  let country = search[0].toUpperCase() + search.substr(1)
  let url = await axios.get(`https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?s=Soccer&c=${country}`)
                            .then(res => res.data)
                            .then(data => data.teams)
                            .then(teams => teams.map(
                              team => ({
                                name: team.strTeam,
                                year: parseInt(team.intFormedYear),
                                stadium: team.strStadium,
                                location: team.strStadiumLocation,
                                capacity: parseInt(team.intStadiumCapacity)})))
                            
  return url
}

main()