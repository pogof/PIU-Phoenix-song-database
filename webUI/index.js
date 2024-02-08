const express = require('express')
const app = express()

const expressLayouts = require('express-ejs-layouts')
const { use } = require('express/lib/application')

app.set('view engine', 'ejs')
app.set('views', __dirname + '/views')
app.set('layout', 'layouts/layout')
app.use(expressLayouts)
app.use(express.static('public'))




//Routes
const indexRouter = require('./routes/index')
//app.use('/:id', indexRouter)
app.use('/', indexRouter)




app.listen(process.env.PORT || 3010)
console.log("listening on port 3010")