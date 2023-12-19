import React, {useState, useEffect} from "react";

export default function NginxConf() {
	const [data, setData] = useState([]);

	useEffect(() => {
		fetch("http://127.0.0.1:8080/api/nginx/conf/")
			.then(response => response.json())
			.then(data => setData(data))
			.catch(error => console.error('Error fetching data:', error));
	}, []);

	return (
		<div>
      <ul>
        {data.map(item => (
          <li key={item.id}>{item.name}: {item.value}</li>
        ))}
      </ul>
    </div>
	);
}
