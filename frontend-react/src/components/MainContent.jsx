import DashboardPage from "./DashboardPage";
import ChatPage from "./ChatPage";
import MemoryPage from "./MemoryPage";
import SettingsPage from "./SettingsPage";

function MainContent({ selectedMenu }) {

  if (selectedMenu === "Dashboard") {
  return (
    <section className="main-content">
      <DashboardPage />
    </section>
  );
}

if (selectedMenu === "Chat") {
  return (
    <section className="main-content">
      <ChatPage />
    </section>
  );
}

if (selectedMenu === "Memory") {
  return (
    <section className="main-content">
      <MemoryPage />
    </section>
  );
}

if (selectedMenu === "Settings") {
  return (
    <section className="main-content">
      <SettingsPage />
    </section>
  );
}

  return (
    <section className="main-content">
      <h1>Page not found</h1>
    </section>
  );
  }

export default MainContent;