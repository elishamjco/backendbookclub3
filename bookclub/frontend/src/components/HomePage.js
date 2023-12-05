import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchAuthenticationStatus = async () => {
            try {
                const response = await fetch('https://localhost:8000/api/', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });

                if (response.ok) {
                    const result = await response.json();
                    setIsAuthenticated(result.isAuthenticated);
                } else {
                    console.error('Failed to fetch authentication status');
                }
            } catch (error) {
                console.error('Error fetching authentication status:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchAuthenticationStatus();
    }, []);

    if (loading) {
        return <p>Loading...</p>;
    }

    return (
        <div>
            <h1>Home</h1>
            {isAuthenticated ? (
                <>
                    <h2><Link to="/add-book">Add Book</Link></h2>
                    <h2><Link to="/add-club">Add Club</Link></h2>
                    <h2><Link to="/clubs">View Clubs</Link></h2>
                    <h2><Link to="/books">View Books</Link></h2>
                    <h2><Link to="/logout">Logout</Link></h2>
                </>
            ) : (
                <>
                    <h2><Link to="/register">Register</Link></h2>
                    <h2><Link to="/login">Login</Link></h2>
                </>
            )}
        </div>
    );
};

export default HomePage;