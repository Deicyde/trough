---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.Immerman.immerman_szelepcsenyi, MetaMathlibExt.Complexity.KeyTheorems.KarpLipton.karp_lipton, MetaMathlibExt.Complexity.KeyTheorems.Ladner.ladner, MetaMathlibExt.Complexity.KeyTheorems.Savitch.savitch
statement: formalized
---

# Complexity classes: its own results

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/index.html).

Definitions of time and space complexity on machine models (P, NP, PSPACE, EXP, L, NL, the polynomial hierarchy, FPT and W[1]), polynomial-time encodings and reductions, simulation overheads, Blum measures, and inclusions and collapses among deterministic and nondeterministic classes (Savitch, Immerman–Szelepcsényi, Karp–Lipton, Ladner, Mahaney). Randomized, counting, circuit and quantum classes have their own fields.

## Immerman-Szelepcsenyi theorem: NL = coNL

The complexity class NL is closed under
complementation: a decision problem $L$ belongs to NL if and only if its complement, the decision
problem that is true exactly on the bitstrings where $L$ is false, belongs to NL.

## Sources

- N. Immerman, "Nondeterministic space is closed under complementation", SIAM Journal on Computing 17 (1988), 935-938; R. Szelepcsenyi, "The method of forced enumeration for nondeterministic automata", Acta Informatica 26 (1988), 279-284.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Immerman.immerman_szelepcsenyi` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/ImmermanWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/index.html#immerman-szelepcsenyi).

## Karp-Lipton theorem: NP in P/poly collapses PH

If every decision problem in NP belongs to
P/poly (polynomial time with polynomial advice), then the polynomial hierarchy PH equals its
second level $\Sigma_2^p$.

## Sources

- R. M. Karp and R. J. Lipton, "Some connections between nonuniform and uniform complexity classes", Proceedings of the Twelfth Annual ACM Symposium on Theory of Computing (STOC 1980), 302-309.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.KarpLipton.karp_lipton` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/KarpLiptonWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/KarpLiptonWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/index.html#karp-lipton).

## Ladner's theorem: NP-intermediate languages exist

If P $\ne$ NP, then there is a decision
problem $L$ in NP that is not in P and to which not every decision problem in NP reduces by a
polynomial-time many-one reduction; that is, $L$ is in NP but is neither in P nor NP-complete.

## Sources

- R. E. Ladner, "On the structure of polynomial time reducibility", Journal of the ACM 22 (1975), 155-171.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Ladner.ladner` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/LadnerWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LadnerWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/index.html#ladner).

## Savitch's theorem: NPSPACE = PSPACE

The complexity class NPSPACE of decision problems
decided in polynomial space by nondeterministic multi-tape Turing machines equals the class
PSPACE of decision problems decided in polynomial space by deterministic multi-tape Turing
machines.

## Sources

- W. J. Savitch, "Relationships between nondeterministic and deterministic tape complexities", Journal of Computer and System Sciences 4 (1970), 177-192.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Savitch.savitch` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/SavitchWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SavitchWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/index.html#savitch).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Complexity classes](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/complexity-classes)
