import logo from "./logo.svg";
import "./App.css";

const Name = () => {
  return(
    <h1>Name</h1>
  )
}

function App() {
  return (
    //In react we have give the class name as "className" because the javascript also has class with oops concept.
    <div className = "heading">
      <Name/>
      <h1>Hi My name is Prasanth.</h1>
    </div>
);
}

export default App;
