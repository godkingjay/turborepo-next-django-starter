import { Metadata } from "next";
import MuiLayout from "ui/Layout/MuiLayout";

export const metadata: Metadata = {
	title: "SorSU - Graduate Tracer System",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
	return (
		<MuiLayout>
			<html lang="en">
				<body>{children}</body>
			</html>
		</MuiLayout>
	);
}
