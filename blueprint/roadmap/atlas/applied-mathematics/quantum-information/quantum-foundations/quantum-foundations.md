---
declaration: section
origin: cited
lean: MathlibExt.QuantumInformation.Finite.KochenSpeckerWanted.kochen_specker_finite_real_three, MathlibExt.QuantumInformation.Finite.TsirelsonTight.tsirelson_bound_tight
statement: formalized
proof: formalized
---

# Quantum foundations: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/index.html).

Quantum foundations studies what quantum mechanics rules out and allows at the level of measurement outcomes, including contextuality, Bell nonlocality and bounds on quantum correlations.

## Kochen–Specker theorem in $\mathbb{R}^3$

There exist a natural number $N$ and unit vectors
$v_1, \dots, v_N \in \mathbb{R}^3$ such that no function $c : \{1, \dots, N\} \to \{0, 1\}$
satisfies both of the following: $c(i) + c(j) \le 1$ whenever $v_i$ and $v_j$ are orthogonal, and
$c(i) + c(j) + c(k) = 1$ whenever $(v_i, v_j, v_k)$ is an orthonormal triple.

## Sources

- S. Kochen, E. P. Specker, The Problem of Hidden Variables in Quantum Mechanics, J. Math. Mech. 17 (1967), 59-87, DOI 10.1512/iumj.1968.17.17004.

Formalized by `MathlibExt.QuantumInformation.Finite.KochenSpeckerWanted.kochen_specker_finite_real_three`, a theorem declared in [MathlibExt/QuantumInformation/Finite/KochenSpecker.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/QuantumInformation/Finite/KochenSpecker.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/index.html#kochen-specker-finite-real-three).

## Tsirelson's bound is attained

There exist $4 \times 4$ complex matrices $A_0, A_1, B_0, B_1$
such that each of them is Hermitian and squares to the identity matrix, each $A_i$ commutes with
each $B_j$, and the CHSH operator $A_0 B_0 + A_0 B_1 + A_1 B_0 - A_1 B_1$ has $2\sqrt{2}$ as an
eigenvalue.

This shows that the upper bound $2\sqrt{2}$ in Tsirelson's inequality for CHSH tuples is sharp.

## Sources

- B. S. Cirel'son/Tsirelson, "Quantum generalizations of Bell's inequality", Lett. Math. Phys. 4 (1980), 93-100, DOI 10.1007/BF00417500.

Formalized by `MathlibExt.QuantumInformation.Finite.TsirelsonTight.tsirelson_bound_tight`, a theorem declared in [MathlibExt/QuantumInformation/Finite/TsirelsonTight.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/QuantumInformation/Finite/TsirelsonTight.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/index.html#tsirelson-bound-tight).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quantum foundations](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/QuantumInformation/quantum-foundations)
