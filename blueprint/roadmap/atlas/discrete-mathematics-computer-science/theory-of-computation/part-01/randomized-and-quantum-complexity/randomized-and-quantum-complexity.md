---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.Adleman.adleman, MetaMathlibExt.Complexity.KeyTheorems.IPEqualsPSPACE.ip_eq_pspace, MetaMathlibExt.Complexity.KeyTheorems.SipserGacs.sipser_gacs_lautemann
statement: formalized
---

# Randomized, interactive and quantum complexity: its own results

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/index.html).

Probabilistic classes (RP, BPP), Arthur–Merlin and interactive proofs (AM, MA, IP = PSPACE, graph (non)isomorphism), BPP versus nonuniform and alternating classes, randomized reductions (Valiant–Vazirani), and quantum classes BQP and QMA.

## Adleman's theorem: BPP is contained in P/poly

Every decision problem in BPP lies in
P/poly.

## Sources

- L. Adleman, "Two theorems on random polynomial time", Proceedings of the Nineteenth Annual Symposium on Foundations of Computer Science (FOCS 1978), 75-83.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Adleman.adleman` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/AdlemanWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/AdlemanWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/index.html#adleman).

## IP = PSPACE (Shamir)

The class $\mathsf{IP}$ of decision problems that have
interactive proofs (a polynomial-time verifier using polynomially many rounds and random coins,
with completeness at least $2/3$ and soundness at most $1/3$ against every prover) equals the
class $\mathrm{PSPACE}$ of decision problems whose languages are decided by multi-tape Turing
machines in polynomial space.

## Sources

- A. Shamir, "IP = PSPACE", Journal of the ACM 39 (1992), 869-877 (FOCS 1990); see also C. Lund, L. Fortnow, H. Karloff, and N. Nisan, "Algebraic methods for interactive proof systems", Journal of the ACM 39 (1992), 859-868.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.IPEqualsPSPACE.ip_eq_pspace` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/IPEqualsPSPACEWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/IPEqualsPSPACEWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/index.html#ip-eq-pspace).

## Sipser-Gács-Lautemann: BPP is in $\Sigma_2^p$ and $\Pi_2^p$

Every decision problem in
BPP lies in $\Sigma_2^p$ and in $\Pi_2^p$, the classes of the polynomial hierarchy defined by two
alternating blocks of polynomially bounded quantifiers, beginning with $\exists$ and with
$\forall$ respectively.

## Sources

- M. Sipser, "A complexity theoretic approach to randomness", Proceedings of the Fifteenth Annual ACM Symposium on Theory of Computing (STOC 1983), 330-335; P. Gács (unpublished); C. Lautemann, "BPP and the polynomial hierarchy", Information Processing Letters 17 (1983), 215-217.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.SipserGacs.sipser_gacs_lautemann` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/SipserGacsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SipserGacsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/index.html#sipser-gacs-lautemann).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Randomized, interactive and quantum complexity](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/randomized-and-quantum-complexity)
