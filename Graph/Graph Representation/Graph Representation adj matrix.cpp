#include <iostream>
using namespace std;

int main() {
	int n, m;

	// Prompting user to enter the number of nodes and edges
	cout << "Enter the number of nodes (n): ";
	cin >> n;

	cout << "Enter the number of edges (m): ";
	cin >> m;

	// Adjacency matrix for undirected graph
	// Initializing the matrix with 0
	int adj[n+1][n+1] = {0}; // Adjust this if nodes are 0-indexed

	cout << "Enter the edges (u v) for each edge:\n";
	for (int i = 0; i < m; i++) {
		int u, v;

		// u and v are the nodes connected by an edge
		cin >> u >> v;
		adj[u][v] = 1;
		adj[v][u] = 1;  // Remove this line in case of a directed graph
	}

	// Print the adjacency matrix
	cout << "\nThe adjacency matrix is:\n";
	for (int i = 1; i <= n; i++) { // Adjust to 0 if nodes are 0-indexed
		for (int j = 1; j <= n; j++) {
			cout << adj[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}
