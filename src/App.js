import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
//  const [playerName, setPlayerName] = useState("");
//  const [goals, setGoals] = useState(0);
//  const [teamName, setTeamName] = useState("");

  const [topScorers, setTopScorers] = useState([])

//  useEffect(() => {
//    fetch('/laliga').then(res => res.json()).then(data => {
//      setTopScorers(data)
//    });
//  }, []);


  function getLeague(league) {
    fetch('/' + league).then(res => res.json()).then(data => {
      console.log(data)
      setTopScorers(data)
    });
  }

  return (
    <div className="App">
      <header className="App-header">

        <h1>Top Scorers</h1>
        <tbody>
          {topScorers.map(player => <tr key={player.playerName}>
            <td className='playerName'>{player.playerName}</td>
            <td className='goals'>{player.goals}</td>
            <td className='teamName'>{player.teamName}</td>
          </tr>)}
        </tbody>
        <div>
          <button className="laliga" onClick={() => getLeague("laliga")}>La Liga</button>
          <button className="bundesliga" onClick={() => getLeague("bundesliga")}>Bundesliga</button>
          <button className="seriea" onClick={() => getLeague("seriea")}>Serie A</button>
          <button className="premierleague" onClick={() => getLeague("premierleague")}>Premier League</button>
          <button className="ligue1" onClick={() => getLeague("ligue1")}>Ligue 1</button>
        </div>
</header>
    </div>
  );
}

export default App;
