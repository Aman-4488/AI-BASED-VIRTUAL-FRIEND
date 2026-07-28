

function Sidebar({ selectedMenu, setSelectedMenu }) {

  const menuItems = [
    {
      id: 1,
      label: "Dashboard",
    },
    {
      id: 2,
      label: "Chat",
    },
    {
      id: 3,
      label: "Memory",
    },
    {
      id: 4,
      label: "Settings",
    },
  ];

  return (
    <aside className="sidebar">

      <div className="sidebar-header">
        <h2>Eunoia</h2>
        <p>Your AI Companion</p>
      </div>

      <div className="menu">

        {menuItems.map((item) => (
          <div
            key={item.id}
            className={`menu-item ${
              selectedMenu === item.label ? "active-menu" : ""
            }`}
            onClick={() => setSelectedMenu(item.label)}
          >
            {item.label}
          </div>
        ))}

      </div>

    </aside>
  );
}

export default Sidebar;