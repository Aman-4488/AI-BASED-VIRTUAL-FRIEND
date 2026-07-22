import "./Header.css";

function Header() {
  return (
    <header className="header">

      <div className="logo">
        <h1>Eunoia</h1>
      </div>

      <nav className="nav-links">
        <a href="#">Dashboard</a>
        <a href="#">Chat</a>
        <a href="#">Settings</a>
      </nav>

      <button className="login-btn">
    Login
      </button>

    </header>
  );
}

export default Header;