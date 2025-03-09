// src/redux/store.ts
import { configureStore } from "@reduxjs/toolkit";
import departmentReducer from "./departmentSlice";
import subjectReducer from "./subjectSlice";

const store = configureStore({
  reducer: {
    departments: departmentReducer, // Reducer for departments
    subjects: subjectReducer, // Reducer for subjects
  },
});

// Log state changes for debugging
store.subscribe(() => {
  console.log("Current Redux State:", store.getState());
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;