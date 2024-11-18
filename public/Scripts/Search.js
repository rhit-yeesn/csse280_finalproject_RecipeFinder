// const mealAPI = "https://www.themealdb.com/api/json/v1/1/"
// const searchName = "search.php?"

// class SearchPage{
//     constructor(form){
//         this.form = form
//         this.results = document.querySelector("#search-results")

//     }

//     activate(){
//         if(this.form == null){
//             return
//         }
//         this.search()
//     }

//     search(){
//         const searchField = this.form.querySelector("input[type=text]")
//         if(searchField){
//             this.form.addEventListener("submit", () =>{
//                 return fetch(`${mealAPI + searchName}` + 
//                     new URLSearchParams({
//                         s: searchField.value.replace(/\s+/g, ""), 
//                         method: "GET",
//                     })
//                 )
//                 .then((response) => {
//                     response.json().then((data) => {
//                         if(data.meals){
//                             this.displaySearchResults(data.meals)
//                         }
//                         else{
//                             this.results.innerHTML = "No results"
//                         }
//                     })
//                 })
//                 .catch((error) => {
//                     console.log("error", error)
//                 })
//             })
//         }
//     }

//     displaySearchResults(meals){
//         this.results.innerHTML = ""
//         meals.forEach(meal => {
//             const template = 
//                 <div class="margin-bottom-30px"> 
//                     <div class="background-white thum-hover box-shadow hvr-float full-width"> 
//                         <div class="float-md-left margin-30px thum-xs"> 
//                             <img class="width-150px search-item-photo" src="${meal.strMealThumb}" alt=""/> 
//                         </div> 
//                         <div class="padding-25px"> 
//                             <div class="rating"> 
//                                 <ul> 
//                                     <li class="active"></li> 
//                                     <li class="active"></li> 
//                                     <li class="active"></li> 
//                                     <li class="active"></li> 
//                                     <li></li> 
//                                 </ul> 
//                             </div> 
//                             <h3>
//                                 <a href="${meal.strSource}" class="d-block text-dark text-capitalize text-medium margin-tb-15px search-item-title">${meal.strMeal}</a>
//                             </h3> 
//                             <hr/> 
//                             <div class="row no-gutters"> 
//                                 <div class="col-4 text-left">
//                                     <a href="#" class="text-red"><i class="far fa-heart"></i> Save</a>
//                                 </div> 
//                                 <div class="col-8 text-right">
//                                     <a href="#" class="text-grey-2"><i class="fas fa-map"></i> ${meal.strArea}</a> 
//                                 </div> 
//                             </div> 
//                         </div> 
//                         <div class="clearfix"></div> 
//                     </div> 
//                 </div>
//         });
//     }
// }

// document.addEventListener("DOMContentLoaded", () => {
//     const form = document.querySelector("#search-form")
//     const search = new SearchPage(form)
//     search.activate()
// })

// export default SearchPage;

import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import Footer from '../../Share/Footer/Footer';
import BrowseByName from '../../Share/BrowseByname/BrowseByName';
import HeaderNav from '../../Share/HeaderNav/HeaderNav';
import GetMealComponents from '../../Share/GetMealComponents/GetMealComponents';

const SearchMeals = () => {
    const { search } = useParams();
    const [meals, setMeals] = useState([]);
    useEffect(() => {
        const url = `https://www.themealdb.com/api/json/v1/1/search.php?s=${search}`;
        axios(url)
            .then(res => {
                if (res.data.meals === null) {
                    setMeals([])
                }
                if (res.data.meals !== null) {
                    setMeals(res.data.meals)
                }
            });
        }, [search])
    return (
        <div className="container">
            {search === 'nothing-search' ?
                    <>
                        <h1 className="text-center text-danger">Sorry You haven't typed anything ...</h1>
                        <div className="text-center">
                            <Link to="/" className="btn btn-success">
                                Return Home
                            </Link>
                        </div>
                    </>
                    :
                    <>
                        <HeaderNav />
                        <div className="mt-5 mb-5 top-border-global-style">
                            <h3 className="text-center mt-3"><b>Your Searching Meals <span className="text-info">"{search}"</span></b></h3>
                            <div className="row">
                                {
                                    meals.map(meal => <GetMealComponents key={meal.idMeal} meal={meal}></GetMealComponents>)
                                }
                            </div>
                        </div>
                        {
                            meals.length === 0 && <h2 className="text-center text-danger">No meals found</h2>
                        }
                        <BrowseByName/>
                        <Footer />
                    </>
            }

        </div>
    );
};

export default SearchMeals;