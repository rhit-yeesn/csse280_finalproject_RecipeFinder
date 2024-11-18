import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import HomePage from './Home';
import RecipeDetails from ' ./RecipeDetails';
import SavedPage from './Saved';
import SearchMeals from './Search';
// import { loadRandomImage } from "./Home";


function App(){
    return (
        <Router>
            <p>This is working</p>
            <div className='App'>    
                <Routes>
                    <Route path="/" element = {<HomePage />}/>
                    <Route path="/recipe/:id" element = {<RecipeDetails />}/>
                    <Route path="/saved" element = {<SavedPage />}/>
                    <Route path="/searchMeals/:search" element = {<SearchPage />}/>
                </Routes>
            </div>
        </Router>
    );
}

export default App;