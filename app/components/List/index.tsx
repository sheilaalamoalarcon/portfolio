import { List } from "../../types/curriculum";

function List(list: List) {
  return (
    <div>
      <h3>{list.title}</h3>
      <ul
        style={{
          textAlign: "justify",
          width: "50%",
        }}
      >
        {list.body.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}
export default List;
