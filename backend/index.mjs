"use strict"
import express from "express"
import cors from "cors"
const app = express();
app.use(cors());
app.use(express.json());


/**
 * Routes
 */
app.get("/", (req,res) => {
    res.send("Invalid Endpoint")
  })
export default app;