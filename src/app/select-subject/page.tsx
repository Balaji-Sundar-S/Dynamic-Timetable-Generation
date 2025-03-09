"use client";

import React, { useState } from "react";
import { Button } from "@/components/ui/ui/button";
import { Input } from "@/components/ui/ui/input";
import { Label } from "@/components/ui/ui/label"; // Import Shadcn components
import { PlusIcon, TrashIcon } from "lucide-react";
import store from "@/redux/store";
import { RootState } from "@/redux/store";
import {useRouter}  from "next/navigation";
import { useDispatch, useSelector } from "react-redux";
import { setSubbyYearAct } from "@/redux/subjectSlice";

// Define types for the data structure
interface Subject {
  code: string;
  name: string;
  credits: string;
}

type YearSubjects = {
  [key: string]: Subject[]; // Map departments to arrays of subjects
};

type SubjectsByYear = {
  [key: string]: YearSubjects; // Map years to departments and their subjects
};

const AddSubjectsPage: React.FC = () => {
  const departments: string[] = store.getState().departments.selectedDepartments; // Get departments from Redux
  const years = ["First Year", "Second Year", "Third Year", "Fourth Year"]; // Available years
  const dispatch = useDispatch();
  // State for tracking the current year and department
  const [currentDepartmentIndex, setCurrentDepartmentIndex] = useState(0);
  const [currentYearIndex, setCurrentYearIndex] = useState(0);

  // State to store subjects for all years and departments
  const [subjectsByYear, setSubjectsByYear] = useState<SubjectsByYear>({});
  const router = useRouter();

  // Add a new subject field for the current year and department
  const addSubjectField = () => {
    const currentYear = years[currentYearIndex];
    const currentDepartment = departments[currentDepartmentIndex];
  
    setSubjectsByYear((prev) => {
      // Create a deep copy of the previous state
      const updatedSubjects = JSON.parse(JSON.stringify(prev));
  
      // Initialize the year and department if they don't exist
      if (!updatedSubjects[currentYear]) {
        updatedSubjects[currentYear] = {};
      }
      if (!updatedSubjects[currentYear][currentDepartment]) {
        updatedSubjects[currentYear][currentDepartment] = [];
      }
  
      // Add a new subject
      updatedSubjects[currentYear][currentDepartment].push({ code: "", name: "", credits: "" });
  
      console.log("Updated Subjects:", updatedSubjects); // Debugging log
      return updatedSubjects;
    });
  };

  // Remove a subject field for the current year and department
  const removeSubjectField = (index: number) => {
    const currentYear = years[currentYearIndex];
    const currentDepartment = departments[currentDepartmentIndex];

    setSubjectsByYear((prev) => {
      const updatedSubjects = { ...prev };
      updatedSubjects[currentYear][currentDepartment] =
        updatedSubjects[currentYear][currentDepartment].filter((_, i) => i !== index);
      return updatedSubjects;
    });
  };

  // Handle changes in subject fields
  const handleSubjectChange = (
    index: number,
    field: keyof Subject,
    value: string
  ) => {
    const currentYear = years[currentYearIndex];
    const currentDepartment = departments[currentDepartmentIndex];

    setSubjectsByYear((prev) => {
      const updatedSubjects = { ...prev };
      const updatedDepartmentSubjects = [...updatedSubjects[currentYear][currentDepartment]];
      updatedDepartmentSubjects[index][field] = value;
      updatedSubjects[currentYear][currentDepartment] = updatedDepartmentSubjects;
      return updatedSubjects;
    });
  };

  // Move to the next year or department
  const moveToNext = () => {
    if (currentYearIndex < years.length - 1) {
      setCurrentYearIndex(currentYearIndex + 1); // Move to the next year
    } else if (currentDepartmentIndex < departments.length - 1) {
      setCurrentDepartmentIndex(currentDepartmentIndex + 1); // Move to the next department
      setCurrentYearIndex(0); // Reset to the first year
    } else {
      alert("All years and departments completed!");
    }
  };

  // Handle form submission
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Subjects by Year and Department:", subjectsByYear);
    dispatch(setSubbyYearAct(subjectsByYear)); // Update the Redux store
    alert("Subjects saved successfully!");
    router.push("/select-faculty")
    // You can send this data to your backend API here
  };


  // Current year and department
  const currentYear = years[currentYearIndex];
  const currentDepartment = departments[currentDepartmentIndex];

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">Add Subjects for All Departments</h1>

      {/* Current Year and Department */}
      <div className="mb-6">
        <h2 className="text-lg font-semibold mb-2">
          {currentYear} - {currentDepartment}
        </h2>
      </div>

      {/* Subject Form */}
      <form onSubmit={handleSubmit}>
        <div className="overflow-x-auto">
          <table className="min-w-full border-separate border-spacing-0 border border-gray-300 rounded-lg">
            <thead>
              <tr className="bg-gray-100">
                <th className="border border-gray-300 px-4 py-2">Subject Code</th>
                <th className="border border-gray-300 px-4 py-2">Subject Name</th>
                <th className="border border-gray-300 px-4 py-2">Credits</th>
                <th className="border border-gray-300 px-4 py-2">Actions</th>
              </tr>
            </thead>
            <tbody>
              {subjectsByYear[currentYear]?.[currentDepartment]?.map((subject, index) => (
                <tr key={index} className="hover:bg-gray-50">
                  <td className="border border-gray-300 px-4 py-2">
                    <Input
                      placeholder="Enter subject code"
                      value={subject.code}
                      onChange={(e) =>
                        handleSubjectChange(index, "code", e.target.value)
                      }
                    />
                  </td>
                  <td className="border border-gray-300 px-4 py-2">
                    <Input
                      placeholder="Enter subject name"
                      value={subject.name}
                      onChange={(e) =>
                        handleSubjectChange(index, "name", e.target.value)
                      }
                    />
                  </td>
                  <td className="border border-gray-300 px-4 py-2">
                    <Input
                      type="number"
                      placeholder="Enter credits"
                      value={subject.credits}
                      onChange={(e) =>
                        handleSubjectChange(index, "credits", e.target.value)
                      }
                    />
                  </td>
                  <td className="border border-gray-300 px-4 py-2 text-center">
                    <button
                      type="button"
                      className="text-red-500 hover:text-red-700"
                      onClick={() => removeSubjectField(index)}
                    >
                      <TrashIcon className="h-5 w-5" />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Add Subject Button */}
        <Button
          type="button"
          variant="outline"
          onClick={addSubjectField} // Ensure this is the only place where addSubjectField is called
          className="mt-4 w-full"
        >
          <PlusIcon className="mr-2 h-4 w-4" /> Add Subject
        </Button>

        {/* Next Button */}
        <Button
          type="button"
          onClick={moveToNext}
          className="mt-6 w-full bg-blue-800"
        >
          Next
        </Button>

        {/* Submit Button */}
        {currentDepartmentIndex === departments.length - 1 &&
        currentYearIndex === years.length - 1 && (
          <Button type="submit" className="mt-6 w-full">
            Save All Subjects
          </Button>
        )}
      </form>
    </div>
  );
};

export default AddSubjectsPage;