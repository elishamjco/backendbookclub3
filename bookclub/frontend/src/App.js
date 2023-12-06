import React, { useState, useEffect } from 'react';
import { Tooltip } from 'react-tooltip';
import 'bootstrap/dist/css/bootstrap.min.css';
import './HomePage.css';

const HomePage = () => {
    const [books, setBooks] = useState([]);
    const [clubs, setClubs] = useState([]);
    const [isDarkMode, setIsDarkMode] = useState(false);

    useEffect(() => {
        fetch('http://localhost:8000/api/books/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error fetching books');
                }
                return response.json();
            })
            .then(data => setBooks(data))
            .catch(error => console.error('Error fetching books:', error));

        fetch('http://localhost:8000/api/clubs/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error fetching clubs');
                }
                return response.json();
            })
            .then(data => setClubs(data))
            .catch(error => console.error('Error fetching clubs:', error));
    }, []);

    const toggleDarkMode = () => {
        setIsDarkMode(!isDarkMode);
    };

    return (
        <div className={`home-page ${isDarkMode ? 'dark-mode' : ''}`}>
            <center>
                <h1>Books</h1>
                <ul>
                    {books.map(book => (
                        <li key={book.id} data-tooltip-id={`my-tooltip-${book.id}`}>
                            Name: {book.book} Description: {book.description}
                            <Tooltip id={`my-tooltip-${book.id}`} place="top" type="info" effect="solid">
                                Author: {book.author}
                            </Tooltip>
                        </li>
                    ))}
                </ul>

                <h1>Clubs</h1>
                <ul>
                    {clubs.map(club => (
                        <li key={club.id}>Name: {club.name} Description: {club.description}</li>
                    ))}
                </ul>

                <button onClick={toggleDarkMode}>{isDarkMode ? 'Light Mode' : 'Dark Mode'}</button>
            </center>
        </div>
    );
};

export default HomePage;