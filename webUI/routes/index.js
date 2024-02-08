const express = require('express')


const {readFileSync} = require('fs')
const jsonToTable = require('json-to-table')

const router = express.Router()


router.get('/', (req, res) => {


  let loadTable = () => {
    let charts = JSON.parse(readFileSync('./public/sorted.json'))
    return charts
  }

  let tabled = loadTable()
  

  //console.log("hello")

  console.log(tabled['stepcharts'][0]['song_name'])





        //res.send("TEST")
        res.render('index', {tabled: tabled})
    
})

module.exports = router