import { Avatar } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
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
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
  BellIcon,
  CalendarIcon,
  MoreVerticalIcon,
  PowerIcon,
  SearchIcon,
} from "lucide-react";
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

const tableHeaders = [
  "Subject",
  "Category",
  "Date Created",
  "Due Date",
  "Account",
];

export default function ClientManagement() {
  return (
    <div className="min-h-screen bg-[#ececec]">
      {/* Header */}
      <header className="h-[120px] bg-[#010529] flex items-center justify-between px-8">
        <h1 className="text-white text-4xl font-bold">Client Management</h1>
        <div className="flex items-center gap-6">
          <Button variant="ghost" size="icon">
            <SearchIcon className="h-6 w-6 text-white" />
          </Button>
          <Button variant="ghost" size="icon">
            <BellIcon className="h-6 w-6 text-white" />
          </Button>
          <Avatar className="h-8 w-8 bg-gray-300" />
          <Button variant="ghost" size="icon">
            <PowerIcon className="h-6 w-6 text-white" />
          </Button>
          <Button variant="ghost" size="icon">
            <MoreVerticalIcon className="h-6 w-6 text-white" />
          </Button>
        </div>
      </header>

      {/* Navigation */}
      <NavigationMenu className="bg-[#d9d9d9] border-b border-[#777777]">
        <NavigationMenuList className="flex justify-start px-4 h-[82px] items-center gap-8">
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
            <Avatar className="h-12 w-12" />
            <h2 className="text-2xl font-bold">Good morning LPL Advisor</h2>
          </div>

          <div className="flex items-center gap-4 mb-6">
            <CalendarIcon className="h-16 w-16" />
            <h2 className="text-4xl font-bold">Client Reminders</h2>
          </div>

          <Tabs defaultValue="birthdays">
            <TabsList className="grid w-[400px] grid-cols-2 bg-[#d9d9d9]">
              <TabsTrigger value="birthdays" className="text-2xl font-bold">
                Birthdays
              </TabsTrigger>
              <TabsTrigger value="anniversaries" className="text-2xl font-bold">
                Anniversaries
              </TabsTrigger>
            </TabsList>
          </Tabs>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-8">
          <div className="flex items-center gap-4 mb-8">
            <BellIcon className="h-12 w-12" />
            <h2 className="text-2xl font-bold">Open Notifications</h2>
          </div>

          <Card>
            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow className="bg-[#d9d9d9]">
                    {tableHeaders.map((header) => (
                      <TableHead
                        key={header}
                        className="text-2xl font-bold text-black"
                      >
                        {header}
                      </TableHead>
                    ))}
                  </TableRow>
                </TableHeader>
                <TableBody>{/* Table content would go here */}</TableBody>
              </Table>
            </CardContent>
          </Card>
        </main>

        {/* Risk Indicator */}
        <aside className="w-[300px] p-4">
          <Card>
            <CardHeader>
              <CardTitle className="text-center">RISK</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="w-48 h-48 mx-auto">
                {/* Placeholder for risk gauge visualization */}
                <div className="rounded-full border-8 border-green-400 w-full h-full flex items-center justify-center">
                  <span className="text-2xl font-bold">Low</span>
                </div>
              </div>
            </CardContent>
          </Card>
        </aside>
      </div>
    </div>
  );
}
