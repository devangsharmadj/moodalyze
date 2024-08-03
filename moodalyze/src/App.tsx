import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  let headers = new Headers()
  headers.append('Access-Control-Allow-Origin', '*');
  headers.append('Access-Control-Allow-Credentials', 'true');

  const [query, setQuery] = useState("")
  const [data, setData] = useState("")
  function handleChange(event) {
    setQuery(event.target.value)
  }

  const queryFetch = () => {
    console.log("Inside the queryfetch")
    fetch('http://127.0.0.1:5000/query?q=' + query).then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }
  // useEffect(() => {
  //   queryFetch();}, []
  // )
  
  // useEffect(() => { 
  //   fetch("/query?q=trump").then(
  //     res => res.json
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data)
  //     }
  //   ), []})

  return (
    <>
     <input onChange={handleChange} id="query-element" type="text"></input>
     <button onClick={queryFetch}></button>
     {data != "" && 
     <div>
      <div>Negative: {data.negative}</div>
      <div>Postitive: {data.positive}</div>
      <div>Neutral: {data.neutral}</div>
     </div>
     }
     
    </>
  )
}

export default App
