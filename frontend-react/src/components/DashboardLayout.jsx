import "./DashboardLayout.css";
import { useState } from "react";

import Sidebar from "./Sidebar";
import MainContent from "./MainContent";
import ContextPanel from "./ContextPanel";

function DashboardLayout() {

  const [selectedMenu, setSelectedMenu] = useState("Dashboard");

  return (
    <main className="dashboard-layout">

      <Sidebar
        selectedMenu={selectedMenu}
        setSelectedMenu={setSelectedMenu}
      />

      <MainContent
        selectedMenu={selectedMenu}
      />

      <ContextPanel />

    </main>
  );
}

export default DashboardLayout;