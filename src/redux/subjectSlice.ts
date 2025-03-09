// src/redux/subjectSlice.ts
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

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

const initialState: SubjectsByYear = {};

const subjectSlice = createSlice({
  name: "subjects",
  initialState,
  reducers: {
    setSubbyYearAct: (state, action: PayloadAction<SubjectsByYear>) => {
      return action.payload; // Replace the entire state with the new data
    },
    addSubject: (
      state,
      action: PayloadAction<{
        year: string;
        department: string;
        subject: Subject;
      }>
    ) => {
      const { year, department, subject } = action.payload;
      if (!state[year]) {
        state[year] = {};
      }
      if (!state[year][department]) {
        state[year][department] = [];
      }
      state[year][department].push(subject);
    },
  },
});

export const { setSubbyYearAct, addSubject } = subjectSlice.actions;

export default subjectSlice.reducer;