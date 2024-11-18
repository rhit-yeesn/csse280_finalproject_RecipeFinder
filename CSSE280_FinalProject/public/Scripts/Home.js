import React, { useEffect, useState } from 'react';
import {Link} from 'react-router-dom';
import axios from 'axios';

function HomePage(){
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(()=>{
    async function fetchRecipes(){
      try{
        const response = await axios.get('/api/recipes');
        setRecipes(response.data.recipes);
        setLoading(false);
      }
      catch(error){
        console.error('Error fetching recipes:', error);
        setLoading(false);
      }
    }

    fetchRecipes();
  }, []);
  return (
    <div>
      <h1>Home Page</h1>
      {loading? (
        <p>Loading...</p>
      ) : (
        <div>
          <p>This is working</p>
          {recipes.map((recipe) =>(
            <div key={recipe.id}>
              <Link to={`/recipe/${recipe.id}`}>
              <h2>{recipe.name}</h2>
              <img src={recipe.image} alt={recipe.name} />
              </Link>
            </div>
          ))}
        </div>
      )}
      <div>
        <button onClick={() => window.location.href = '/'}>Home</button>
        <button onClick={() => window.location.href = '/saved'}>Saved</button>
      </div>
    </div>
  );
}

export default HomePage;

