"use client";

import React, { useState } from "react";
import { Button } from "@/components/ui/ui/button";
import { Input } from "@/components/ui/ui/input";
import { Label } from "@/components/ui/ui/label"; // Import Shadcn components
import { PlusIcon, TrashIcon } from "lucide-react";
import store from "@/redux/store";
import { RootState } from "@/redux/store";
import { useSelector } from "react-redux";

// Define types for the data structure
interface Subject {
  code: string;
  name: string;
  credits: string;
  faculties: string[]; // Array of faculty names
}

type YearSubjects = {
  [key: string]: Subject[]; // Map departments to arrays of subjects
};

type SubjectsByYear = {
  [key: string]: YearSubjects; // Map years to departments and their subjects
};

const AssignFacultiesPage: React.FC = () => {
  const subjectsByYear: SubjectsByYear = useSelector(
    (state: RootState) => state.subjects.subjectsByYear
  ); // Get subjects from Redux

  // State to store updated subjects with faculties
  const [updatedSubjects, setUpdatedSubjects] = useState<SubjectsByYear>(subjectsByYear);

  // Add a new faculty field for a specific subject
  const addFacultyField = (year: string, department: string, subjectIndex: number) => {
    setUpdatedSubjects((prev) => {
      const updatedSubjects = JSON.parse(JSON.stringify(prev)); // Deep copy
      updatedSubjects[year][department][subjectIndex].faculties.push("");
      return updatedSubjects;
    });
  };

  // Remove a faculty field for a specific subject
  const removeFacultyField = (
    year: string,
    department: string,
    subjectIndex: number,
    facultyIndex: number
  ) => {
    setUpdatedSubjects((prev) => {
      const updatedSubjects = JSON.parse(JSON.stringify(prev)); // Deep copy
      updatedSubjects[year][department][subjectIndex].faculties.splice(facultyIndex, 1);
      return updatedSubjects;
    });
  };

  // Handle changes in faculty fields
  const handleFacultyChange = (
    year: string,
    department: string,
    subjectIndex: number,
    facultyIndex: number,
    value: string
  ) => {
    setUpdatedSubjects((prev) => {
      const updatedSubjects = JSON.parse(JSON.stringify(prev)); // Deep copy
      updatedSubjects[year][department][subjectIndex].faculties[facultyIndex] = value;
      return updatedSubjects;
    });
  };

  // Handle form submission
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Subjects with Assigned Faculties:", updatedSubjects);
    // You can send this data to your backend API here
  };

  // Convert subjectsByYear into an array for easier iteration
  const yearsArray = Object.entries(updatedSubjects); // Convert years to an array of [key, value] pairs

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">Assign Faculties to Subjects</h1>

      {/* Form */}
      <form onSubmit={handleSubmit}>
        {yearsArray.map(([year, departments]) => (
          <div key={year} className="mb-8">
            <h2 className="text-xl font-semibold mb-4">{year}</h2>
            {Object.entries(departments).map(([department, subjects]) => (
              <div key={department} className="mb-6">
                <h3 className="text-lg font-medium mb-2">{department}</h3>
                <div className="overflow-x-auto">
                  <table className="min-w-full border-separate border-spacing-0 border border-gray-300 rounded-lg">
                    <thead>
                      <tr className="bg-gray-100">
                        <th className="border border-gray-300 px-4 py-2">Subject Code</th>
                        <th className="border border-gray-300 px-4 py-2">Subject Name</th>
                        <th className="border border-gray-300 px-4 py-2">Credits</th>
                        <th className="border border-gray-300 px-4 py-2">Assigned Faculties</th>
                        <th className="border border-gray-300 px-4 py-2">Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {subjects.map((subject, subjectIndex) => (
                        <tr key={subjectIndex} className="hover:bg-gray-50">
                          <td className="border border-gray-300 px-4 py-2">{subject.code}</td>
                          <td className="border border-gray-300 px-4 py-2">{subject.name}</td>
                          <td className="border border-gray-300 px-4 py-2">{subject.credits}</td>
                          <td className="border border-gray-300 px-4 py-2">
                            {subject.faculties.map((faculty, facultyIndex) => (
                              <div key={facultyIndex} className="flex items-center space-x-2 mb-2">
                                <Input
                                  placeholder="Enter faculty name"
                                  value={faculty}
                                  onChange={(e) =>
                                    handleFacultyChange(
                                      year,
                                      department,
                                      subjectIndex,
                                      facultyIndex,
                                      e.target.value
                                    )
                                  }
                                />
                                <button
                                  type="button"
                                  className="text-red-500 hover:text-red-700"
                                  onClick={() =>
                                    removeFacultyField(year, department, subjectIndex, facultyIndex)
                                  }
                                >
                                  <TrashIcon className="h-5 w-5" />
                                </button>
                              </div>
                            ))}
                            {/* Add Faculty Button */}
                            <Button
                              type="button"
                              variant="outline"
                              onClick={() => addFacultyField(year, department, subjectIndex)}
                              className="mt-2 w-full"
                            >
                              <PlusIcon className="mr-2 h-4 w-4" /> Add Faculty
                            </Button>
                          </td>
                          <td className="border border-gray-300 px-4 py-2 text-center">
                            {/* Placeholder for additional actions */}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            ))}
          </div>
        ))}

        {/* Submit Button */}
        <Button type="submit" className="mt-6 w-full">
          Save All Assignments
        </Button>
      </form>
    </div>
  );
};

export default AssignFacultiesPage;