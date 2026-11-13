---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SumsetInPositiveDensityErdosProblem109Wanted.sumsetInPositiveUpperDensity, MathlibExt.Combinatorics.SumsetInPositiveDensityErdosProblem109Wanted.sumsetInPositiveUpperDensity_holds
statement: formalized
---

# Erdős sumset conjecture

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/erd-s-sumset-conjecture/index.html).

## Erdős Problem 109 (the Erdős sumset conjecture)

The upper density of a set
$A \subseteq \mathbb{N}$ is $\limsup_{N \to \infty} \lvert A \cap \{0, \dots, N - 1\} \rvert / N$.
This is the statement that every set $A \subseteq \mathbb{N}$ of positive upper density contains
$B + C = \{b + c \mid b \in B, c \in C\}$ for some infinite sets $B, C \subseteq \mathbb{N}$.

Formalized by `MathlibExt.Combinatorics.SumsetInPositiveDensityErdosProblem109Wanted.sumsetInPositiveUpperDensity`, a definition declared in [WantedExt/Combinatorics/SumsetInPositiveDensityErdosProblem109Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetInPositiveDensityErdosProblem109Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/erd-s-sumset-conjecture/index.html#sumset-in-positive-upper-density).

## Moreira–Richter–Robertson theorem (the Erdős sumset conjecture)

The upper density of a
set $A \subseteq \mathbb{N}$ is
$\limsup_{N \to \infty} \lvert A \cap \{0, \dots, N - 1\} \rvert / N$. Every set
$A \subseteq \mathbb{N}$ of positive upper density contains
$B + C = \{b + c \mid b \in B, c \in C\}$ for some infinite sets $B, C \subseteq \mathbb{N}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #109, https://www.erdosproblems.com/109 (status PROVED (LEAN)); resolution: J. Moreira, F. K. Richter and D. Robertson, A proof of a sumset conjecture of Erdős, Ann. of Math. (2) (2019), 605-652, main theorem (erdosproblems.com/109), https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos109.lean#L9074.

Stated but not proved: `MathlibExt.Combinatorics.SumsetInPositiveDensityErdosProblem109Wanted.sumsetInPositiveUpperDensity_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetInPositiveDensityErdosProblem109Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SumsetInPositiveDensityErdosProblem109Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/erd-s-sumset-conjecture/index.html#sumset-in-positive-upper-density-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Erdős sumset conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/erd-s-sumset-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/erd-s-sumset-conjecture)
