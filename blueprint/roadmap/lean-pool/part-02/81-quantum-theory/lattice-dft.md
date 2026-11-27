---
declaration: theorem
origin: cited
lean: DFT.generic_hk_lattice_fermions_w, DFT.dimH_nonUVDens_lattice_fermions_w, DFT.ks_potential_exists_interior, DFT.lattice_myksoda
statement: formalized
proof: formalized
---

# Density-functional theory for lattice fermions

> Develops density-functional theory for spinless fermions on finite graphs. It proves generic uniqueness of the potential up to a constant, bounds the Hausdorff dimension of exceptional densities, and develops lattice Kohn–Sham representability. It proves full regularized energy convergence and potential convergence along convergent quasi-density subsequences.

*Quoted from the card [LeanPool/projects/lattice-dft.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/lattice-dft.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`DFT.generic_hk_lattice_fermions_w`](https://leanpool.github.io/lean-pool/LeanPool/DFT/Lattice/GenericHK.html#DFT.generic_hk_lattice_fermions_w) (theorem; a main declaration), declared in [LeanPool/DFT/Lattice/GenericHK.lean, line 205](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DFT/Lattice/GenericHK.lean#L205): “For N spinless fermions on a connected M-site graph, assume 0 < N < M, symmetric hopping of a common sign on the edges, and interactions diagonal in the occupation basis. The potentials whose ground state is shared by a potential differing by more than a constant lie in a closed, nowhere dense, Lebesgue-null set.”
- [`DFT.dimH_nonUVDens_lattice_fermions_w`](https://leanpool.github.io/lean-pool/LeanPool/DFT/Lattice/Generic/DensityDim/Fermions.html#DFT.dimH_nonUVDens_lattice_fermions_w) (theorem; a main declaration), declared in [LeanPool/DFT/Lattice/Generic/DensityDim/Fermions.lean, line 78](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DFT/Lattice/Generic/DensityDim/Fermions.lean#L78): “For N spinless fermions with 0 < N < M on a connected M-site graph, assume symmetric common-sign edge hopping and an interaction diagonal in the occupation basis. Densities of normalized, nondegenerate ground states shared with a second potential differing by more than a constant have Hausdorff dimension at most M minus three, truncated at zero.”
- [`DFT.ks_potential_exists_interior`](https://leanpool.github.io/lean-pool/LeanPool/DFT/Lattice/KohnSham/Hypersimplex.html#DFT.ks_potential_exists_interior) (theorem; a main declaration), declared in [LeanPool/DFT/Lattice/KohnSham/Hypersimplex.lean, line 190](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DFT/Lattice/KohnSham/Hypersimplex.lean#L190): “For N spinless fermions on an M-site graph with 0 < N < M, fix any uniform real hopping amplitude on that graph. A density with each occupation strictly between zero and one and total occupation N is realized by a ground-state ensemble for a site potential of the noninteracting Hamiltonian with that hopping.”
- [`DFT.lattice_myksoda`](https://leanpool.github.io/lean-pool/LeanPool/DFT/Lattice/KohnSham/RegularizedKS.html#DFT.lattice_myksoda) (theorem; a main declaration), declared in [LeanPool/DFT/Lattice/KohnSham/RegularizedKS.lean, line 178](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DFT/Lattice/KohnSham/RegularizedKS.lean#L178): “Take a positive regularization parameter and real symmetric interacting and reference Hamiltonians on the same nonempty finite configuration space with a common occupation map. For sequences satisfying the MYKSODA update equations, the regularized energy is nonincreasing and the full energy sequence converges to its minimum. The quasi-density sequence has an accumulation point. Along each convergent quasi-density subsequence, the corresponding Kohn–Sham potentials converge to a potential yielding a minimizing reference density.”

## Project

- Authors: Miguel A. L. Marques, Stefano Pittalis.
- Source: *Lattice density-functional theory in Lean*.
- Project repository: [hyllios/lean_dft](https://github.com/hyllios/lean_dft), at commit [144b0dca](https://github.com/hyllios/lean_dft/tree/144b0dca3e597f2ae021f1c1b263ceab857f8f26).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 81V55, 81Q10, 90C25.
- In Lean Pool: [LeanPool/DFT](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DFT), from the card [LeanPool/projects/lattice-dft.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/lattice-dft.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/lattice-dft.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/lattice-dft.yaml)
- [Lean Pool at bb99e52c: LeanPool/DFT](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DFT)
