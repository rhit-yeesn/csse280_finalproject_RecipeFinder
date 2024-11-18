import React from 'react';

function SavedPage() {
    return (
        <div>
            <h1>Saved Recipes</h1>
            <div>
                <button onClick={() => window.location.href = '/'}>Home</button>
                <button onClick={() => window.location.href = '/saved'}>Saved</button>
            </div>
        </div>
    );
}

export default SavedPage;