import "./Header.css";

function Header() {
  return (
    <header className="header">

      <div className="logo">
        Eunoia
      </div>

      <nav className="nav-links">
        <a href="#">Home</a>
        <a href="#">Features</a>
        <a href="#">About</a>
      </nav>

      <button className="login-btn">
        Login
      </button>

    </header>
  );
}

export default Header;