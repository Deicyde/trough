---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.SimplicityConjectureWanted.SimplicityConjecture.Homeo, MathlibExt.Dynamics.SimplicityConjectureWanted.SimplicityConjecture.theorem_1_2
statement: formalized
---

# Simplicity conjecture

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/simplicity-conjecture/index.html).

## Area-preserving homeomorphisms of the disc supported in the interior

Let $\mathbb{D}$ be
the closed unit disc in $\mathbb{R}^2$ and let $\omega$ be the restriction of Lebesgue measure to
$\mathbb{D}$. $\mathrm{Homeo}_c(\mathbb{D}, \omega)$ is the subgroup of the group of
homeomorphisms of $\mathbb{D}$ consisting of the homeomorphisms $\phi$ that preserve $\omega$ and
whose support, the closure of $\{x \in \mathbb{D} : \phi(x) \neq x\}$, is contained in the open
unit disc.

Formalized by `MathlibExt.Dynamics.SimplicityConjectureWanted.SimplicityConjecture.Homeo`, a definition declared in [WantedExt/Dynamics/SimplicityConjectureWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/SimplicityConjectureWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/simplicity-conjecture/index.html#homeo).

## Simplicity conjecture

Let $\mathbb{D} \subseteq \mathbb{R}^2$ be the closed unit disc and let
$\omega$ be the restriction of Lebesgue measure to $\mathbb{D}$. The group
$\mathrm{Homeo}_c(\mathbb{D}, \omega)$ of homeomorphisms of $\mathbb{D}$ that preserve $\omega$
and whose support, the closure of the set of non-fixed points, lies in the open unit disc is not
simple: it is trivial or it has a normal subgroup other than the trivial subgroup and the whole
group.

## Sources

- D. Cristofaro-Gardiner, V. Humilière, and S. Seyfaddini, `Proof of the simplicity conjecture`, Annals of Math, 199 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_simplicity_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.SimplicityConjectureWanted.SimplicityConjecture.theorem_1_2` is written with `theorem_wanted` in [WantedExt/Dynamics/SimplicityConjectureWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/SimplicityConjectureWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/simplicity-conjecture/index.html#theorem-1-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simplicity conjecture](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/simplicity-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/low-dimensional-dynamics/simplicity-conjecture)
