import React from "react";
import { CardEvento } from "../component/CardEvento.jsx";
import "../../styles/HomePage.css";

const HomePage = () => {
    return (
        <div class="container py-5">
            <h1 class="text-center">Próximos eventos</h1>
            <div class="row row-cols-1 row-cols-md-3 g-4 py-5">
                <CardEvento />
                <CardEvento />
                <CardEvento />
                <CardEvento />
                <CardEvento />
                <CardEvento />
                <CardEvento />
                <CardEvento />
                <CardEvento />
            </div>
        </div>
    )
};
export default HomePage;