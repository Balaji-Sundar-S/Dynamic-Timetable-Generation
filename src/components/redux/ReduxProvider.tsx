// src/components/ReduxProvider.tsx
"use client"; // Mark this as a Client Component

import React from "react";
import { Provider } from "react-redux";
import store from "@/redux/store";

export const ReduxProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return <Provider store={store}>{children}</Provider>;
};