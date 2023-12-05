import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './components/HomePage';
import AddBook from './components/AddBook';
import AddClub from './components/AddClub';
import ViewClubs from './components/ViewClubs';
import ViewBooks from './components/ViewBooks';
import Login from './components/Login';
import Register from './components/Register';
import BookDetails from './components/BookDetails';
import ClubDetails from './components/ClubDetails';
import PostReview from './components/PostReview';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={HomePage} />
                <Route path="/add-book" component={AddBook} />
                <Route path="/add-club" component={AddClub} />
                <Route path="/clubs" component={ViewClubs} />
                <Route path="/books" component={ViewBooks} />
                <Route path="/login" component={Login} />
                <Route path="/register" component={Register} />
                <Route path="/bookdetails/:bookId" component={BookDetails} />
                <Route path="/clubdetails/:clubId" component={ClubDetails} />
                <Route path="/postreview" component={PostReview} />
            </Switch>
        </Router>
    );
};

export default App;