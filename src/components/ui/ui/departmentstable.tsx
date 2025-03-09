"use client"; // This is necessary if you're using Next.js with server components

import React, { useState } from "react";
import { useDispatch } from "react-redux"; // Import useDispatch
import {setSelectedDepartments}  from "@/redux/departmentSlice"; // Import the Redux action
import { Input } from "@/components/ui/ui/input"; // Import shadcn Input component
import { Button } from "@/components/ui/ui/button"; // Import shadcn Button component
import { X } from "lucide-react"; // Import cross icon from Lucide Icons
import { useRouter } from "next/navigation";

export default function DepartmentsTable() {
  const [inputValue, setInputValue] = useState(""); // State for the input field
  const [rows, setRows] = useState<string[]>([]); // State for the list of rows
  const dispatch = useDispatch(); // Get the dispatch function from Redux
  const router = useRouter();

  // Function to handle adding a new row
  const handleAddRow = () => {
    if (inputValue.trim() !== "") {
      setRows((prevRows) => [...prevRows, inputValue.trim()]); // Add the input value to the rows list
      setInputValue(""); // Clear the input field
    }
  };

  // Function to handle removing a row
  const handleRemoveRow = (index: number) => {
    setRows((prevRows) => prevRows.filter((_, i) => i !== index)); // Remove the row at the given index
  };

  // Function to handle submitting rows to Redux
  const handleSubmit = () => {
    dispatch(setSelectedDepartments(rows)); // Dispatch the action to store the rows in Redux
    console.log("Rows submitted to Redux:", rows);
    router.push("/select-subject");
  };

  return (
    <div className="flex flex-col items-center justify-center mt-5">
      {/* Input Field */}
      <div className="flex space-x-2 mb-4">
        <Input
          type="text"
          placeholder="Enter something..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)} // Update state on change
          onKeyDown={(e) => e.key === "Enter" && handleAddRow()} // Add row on Enter key press
          className="w-64" // Optional styling
        />
        <Button className="bg-blue-800" onClick={handleAddRow}>
          Add
        </Button>
      </div>

      {/* Table */}
      <div className="w-full max-w-md">
        <table className="min-w-full border-separate border-spacing-0 border-2 border-blue-800 rounded-lg overflow-hidden">
          <thead>
            <tr className="bg-blue-800">
              <th className="border border-blue-800 text-white px-4 py-2">Department</th>
            </tr>
          </thead>
          <tbody>
            {rows.length > 0 ? (
              rows.map((row, index) => (
                <tr key={index} className="hover:bg-blue-100">
                  <td className="border border-blue-800 px-4 py-2 flex justify-between">
                    {row}
                    <button
                      onClick={() => handleRemoveRow(index)}
                      className="text-blue-800 hover:text-blue-300"
                    >
                      <X size={16} /> {/* Cross icon */}
                    </button>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={2} className="border border-blue-800 px-4 py-2 text-center">
                  No data available
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {/* Submit Button */}
      <Button className="bg-blue-800 mt-5 w-64" onClick={handleSubmit}>
        Submit
      </Button>
    </div>
  );
}