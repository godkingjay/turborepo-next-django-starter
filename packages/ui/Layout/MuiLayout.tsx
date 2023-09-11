"use client";

import { CssBaseline } from "@mui/material";
import React from "react";

type MuiLayoutProps = {
	children: React.ReactNode;
};

const MuiLayout: React.FC<MuiLayoutProps> = (props) => {
	const { children } = props;

	return (
		<>
			<CssBaseline />
			{children}
		</>
	);
};

export default MuiLayout;
