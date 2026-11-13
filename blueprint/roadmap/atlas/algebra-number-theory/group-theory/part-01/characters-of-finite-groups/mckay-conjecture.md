---
declaration: section
origin: cited
lean: MetaMathlibExt.pPrimeCharacters, MetaMathlibExt.mckay_irr_equicardinal
statement: formalized
---

# McKay conjecture

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/mckay-conjecture/index.html).

## Irreducible characters of $p'$-degree

For a group $G$ and a natural number $p$,
$\mathrm{Irr}_{p'}(G)$ is the set of functions $G \to \mathbb{C}$ that are characters of simple
finite-dimensional complex representations of $G$ whose dimension is not divisible by $p$.

Two simple representations have equal characters exactly when they are isomorphic, so these
characters correspond bijectively to the isomorphism classes of such representations, which is
what the McKay conjecture counts.

Formalized by `MetaMathlibExt.pPrimeCharacters`, a definition declared in [WantedExt/GroupTheory/McKayConjectureWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/McKayConjectureWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/mckay-conjecture/index.html#p-prime-characters).

## McKay conjecture (Cabanes–Späth theorem)

For every finite group $G$, every prime $p$ and
every Sylow $p$-subgroup $P$ of $G$, with normalizer $N_G(P)$ in $G$, the sets
$\mathrm{Irr}_{p'}(G)$ and $\mathrm{Irr}_{p'}(N_G(P))$ of irreducible complex characters of
degree not divisible by $p$ have the same cardinality.

## Sources

- M. Cabanes and B. Späth, *The McKay conjecture*, Ann. of Math. 203(3) (2026), arXiv:2410.20392, doi:10.4007/annals.2026.203.3.5.

Stated but not proved: `MetaMathlibExt.mckay_irr_equicardinal` is written with `theorem_wanted` in [WantedExt/GroupTheory/McKayConjectureWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/McKayConjectureWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/mckay-conjecture/index.html#mckay-irr-equicardinal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: McKay conjecture](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/mckay-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/characters-of-finite-groups/mckay-conjecture)
