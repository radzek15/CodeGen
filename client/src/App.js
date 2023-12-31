import React from "react";
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import 'mdb-react-ui-kit/dist/css/mdb.min.css';
import "@fortawesome/fontawesome-free/css/all.min.css";

import NginxGen from "./pages/nginxGen";
import HomePage from "./pages/HomePage";
import DockerGen from "./pages/DockerGen";
import DockerComposeGen from "./pages/DockerComposeGen";

function App() {
  const router = createBrowserRouter([
    { path: '/', element: <HomePage /> },
    { path: '/docker', element: <DockerGen /> },
    { path: '/docker-compose', element: <DockerComposeGen/> },
    { path: '/nginx', element: <NginxGen /> }
  ])

  return (
    <div>
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
