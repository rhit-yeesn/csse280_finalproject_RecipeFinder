import React, {useEffect, useState} from 'react';
import {useParams} from 'react-router-dom';
import axios from 'axios';

function RecipeDetails(){
    const {id} = useParams();
    const{recipe, setRecipe} = useState(null);
    constt [loading, setLoading] = useState(true);

    useEffect(() => {
        async function fetchRecipeDetails(){
            try{
                const response = await axios.get(`/api/recipes/${id}`);
                setRecipe(response.data.recipe);
                setLoading(false);
            }
            catch(error){
                console.error('Error fetching recipe details:', error);
                setLoading(false);
            }
        }
        fetchRecipeDetails();
    }, [id]);

    return (
        <div>
            <h1>Recipe Details</h1>
            {loading ? (
                <p>Loading...</p>
            ) : recipe ? (
                <div>
                    <h2>{recipe.name}</h2>
                    <img src={recipe.image} alt={recipe.name} />
                    <p>{recipe.instructions}</p>
                </div>
            ) : (
                <p>Recipe Not Found.</p>
            )}
            <div>
                <button onClick={() => window.location.href = '/'}>Home</button>
                <button onClick={() => window.location.href = '/saved'}>Saved</button>
            </div>
        </div>
    );
}

export default RecipeDetails;