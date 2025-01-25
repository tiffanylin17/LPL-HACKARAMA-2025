import React, { useState } from "react";

function App() {
  const [responseData, setResponseData] = useState(null); // State to hold the response
  const [loading, setLoading] = useState(false); // State for loading indicator


  import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
} from "@/components/ui/navigation-menu";
import {
  Table,
  TableBody,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Bell, Calendar, Menu, Search, Settings } from "lucide-react";
import React from "react";

const navigationItems = [
  "Home",
  "Practice Metrics",
  "Groups",
  "Clients",
  "Accounts",
  "Investments",
  "Orders",
  "Activity",
  "Requests",
  "Documents",
];

export default function ClientManagement() {
  return (
    <div className="min-h-screen bg-[#ececec]">
      {/* Header */}
      <header className="h-[120px] bg-[#010529] flex items-center justify-between px-8">
        <h1 className="text-white text-4xl font-bold">Client Management</h1>
        <div className="flex items-center gap-6">
          <Search className="w-6 h-6 text-white" />
          <Bell className="w-6 h-6 text-white" />
          <div className="w-[54px] h-[35px] bg-[#d9d9d9] rounded-full" />
          <Settings className="w-6 h-6 text-white" />
          <Menu className="w-6 h-6 text-white" />
        </div>
      </header>

      {/* Navigation */}
      <NavigationMenu className="w-full bg-[#d9d9d9] border-b border-[#777777]">
        <NavigationMenuList className="flex justify-start px-4 py-6 gap-8">
          {navigationItems.map((item) => (
            <NavigationMenuItem key={item}>
              <NavigationMenuLink className="text-[#3f3f3f] font-bold text-2xl hover:text-black">
                {item}
              </NavigationMenuLink>
            </NavigationMenuItem>
          ))}
        </NavigationMenuList>
      </NavigationMenu>

      <div className="flex">
        {/* Sidebar */}
        <aside className="w-[494px] bg-[#d9d9d9] min-h-[917px] p-6">
          <div className="flex items-center gap-4 mb-12">
            <img src="" alt="Profile" className="w-[41px] h-[43px]" />
            <h2 className="text-3xl font-bold">Good morning LPL Advisor</h2>
          </div>

          <div className="flex items-center gap-4 mb-6">
            <Calendar className="w-[71px] h-[70px]" />
            <h3 className="text-4xl font-bold">Client Reminders</h3>
          </div>

          <div className="flex gap-4">
            <Button variant="ghost" className="text-2xl font-bold">
              Birthdays
            </Button>
            <Button variant="ghost" className="text-2xl font-bold">
              Anniversaries
            </Button>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-8">
          <div className="flex items-center gap-4 mb-8">
            <Bell className="w-[60px] h-[60px]" />
            <h2 className="text-2xl font-bold">Open Notifications</h2>
          </div>

          <Card>
            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow className="bg-[#d9d9d9]">
                    <TableHead className="font-bold text-2xl text-black">
                      Subject
                    </TableHead>
                    <TableHead className="font-bold text-2xl text-black">
                      Category
                    </TableHead>
                    <TableHead className="font-bold text-2xl text-black">
                      Date Created
                    </TableHead>
                    <TableHead className="font-bold text-2xl text-black">
                      Due Date
                    </TableHead>
                    <TableHead className="font-bold text-2xl text-black">
                      Account
                    </TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {/* Table content would be populated here */}
                </TableBody>
              </Table>
            </CardContent>
          </Card>
        </main>

        {/* Risk Indicator */}
        <aside className="w-[255px] p-4">
          <Card>
            <CardContent>
              <img
                src=""
                alt="Risk Indicator"
                className="w-full h-[221px] object-cover"
              />
            </CardContent>
          </Card>
        </aside>
      </div>
    </div>
  );
}


  return (
    <div style={{ padding: "20px" }}>
      <h1>Test API Endpoint</h1>
      <button onClick={handleButtonClick} disabled={loading}>
        {loading ? "Loading..." : "Send Request"}
      </button>
      <div style={{ marginTop: "20px" }}>
        <h2>Response:</h2>
        <pre>{responseData ? JSON.stringify(responseData, null, 2) : "No response yet"}</pre>
      </div>
    </div>
  );
}

export default App;
