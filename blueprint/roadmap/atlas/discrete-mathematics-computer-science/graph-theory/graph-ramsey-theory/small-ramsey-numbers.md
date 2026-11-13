---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_four_four, MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.forty_three_le_graphRamsey_five_five, MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_five_five_le_forty_six, MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_five, MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_six, MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_seven, MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_eight, MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_nine
statement: formalized
---

# Small Ramsey numbers

10 results, 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html).

## The value of $R(4, 4)$

The classical Ramsey number $R(4, 4)$ equals $18$.

## Sources

- R. E. Greenwood and A. M. Gleason, *Combinatorial relations and chromatic graphs*, Canad. J. Math. 7 (1955), 1–7; S. P. Radziszowski, *Small Ramsey Numbers*, Electron. J. Combin. Dynamic Survey DS1; listed in leansolving/SqueezeBench `SqueezeBench/Problems/Ramsey/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_four_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html#graph-ramsey-four-four).

## Exoo's lower bound for $R(5, 5)$

The classical Ramsey number $R(5, 5)$ is at
least $43$.

Thus some simple graph on $42$ vertices contains no $K_5$ and no independent set of size $5$.

## Sources

- G. Exoo, *A lower bound for R(5,5)*, J. Graph Theory 13 (1989), 97–98; Radziszowski, DS1; listed in SqueezeBench `SqueezeBench/Problems/Ramsey/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.forty_three_le_graphRamsey_five_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html#forty-three-le-graph-ramsey-five-five).

## The Angeltveit–McKay upper bound for $R(5, 5)$

The classical Ramsey number
$R(5, 5)$ is at most $46$.

## Sources

- V. Angeltveit and B. D. McKay, *R(5,5) ≤ 46*, arXiv:2409.15709 (2024); listed in SqueezeBench `SqueezeBench/Problems/Ramsey/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_five_five_le_forty_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html#graph-ramsey-five-five-le-forty-six).

## The value of $R(3, 5)$

The classical Ramsey number $R(3, 5)$ equals $14$.

## Sources

- Greenwood and Gleason (1955), op. cit.; Radziszowski, DS1; OEIS A000791; listed in SqueezeBench `SqueezeBench/Problems/Ramsey3/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html#graph-ramsey-three-five).

## The value of $R(3, 6)$

The classical Ramsey number $R(3, 6)$ equals $18$.

## Sources

- G. Kéry, *On a theorem of Ramsey*, Mat. Lapok 15 (1964), 204–224 (upper bound), with the lower bound from Kalbfleisch (1966); Radziszowski, DS1; OEIS A000791; listed in SqueezeBench `SqueezeBench/Problems/Ramsey3/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html#graph-ramsey-three-six).

## The value of $R(3, 7)$

The classical Ramsey number $R(3, 7)$ equals $23$.

## Sources

- J. G. Kalbfleisch, *Chromatic graphs and Ramsey's theorem*, Ph.D. thesis, University of Waterloo (1966) (lower bound); J. E. Graver and J. Yackel, *Some graph theoretic results associated with Ramsey's theorem*, J. Combin. Theory 4 (1968), 125–175 (upper bound); Radziszowski, DS1; OEIS A000791; listed in SqueezeBench `SqueezeBench/Problems/Ramsey3/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_seven` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html#graph-ramsey-three-seven).

## The value of $R(3, 8)$

The classical Ramsey number $R(3, 8)$ equals $28$.

## Sources

- C. Grinstead and S. Roberts, *On the Ramsey numbers R(3,8) and R(3,9)*, J. Combin. Theory Ser. B 33 (1982), 27–51 (lower bound); B. D. McKay and Zhang Ke Min, *The value of the Ramsey number R(3,8)*, J. Graph Theory 16 (1992), 99–105 (upper bound); Radziszowski, DS1; OEIS A000791; listed in SqueezeBench `SqueezeBench/Problems/Ramsey3/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html#graph-ramsey-three-eight).

## The value of $R(3, 9)$

The classical Ramsey number $R(3, 9)$ equals $36$.

## Sources

- Kalbfleisch (1966), op. cit. (lower bound); Grinstead and Roberts (1982), op. cit. (upper bound); Radziszowski, DS1; OEIS A000791; listed in SqueezeBench `SqueezeBench/Problems/Ramsey3/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_nine` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html#graph-ramsey-three-nine).

## Exoo's lower bound for $R(3, 10)$

The classical Ramsey number $R(3, 10)$ is at
least $40$.

## Sources

- G. Exoo, *On two classical Ramsey numbers of the form R(3,n)*, SIAM J. Discrete Math. 2 (1989), 488–490; Radziszowski, DS1; listed in SqueezeBench `SqueezeBench/Problems/Ramsey3/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.forty_le_graphRamsey_three_ten` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html#forty-le-graph-ramsey-three-ten).

## Angeltveit's upper bound for $R(3, 10)$

The classical Ramsey number $R(3, 10)$
is at most $41$.

## Sources

- V. Angeltveit, *R(3,10) ≤ 41*, arXiv:2401.00392 (2024); Radziszowski, DS1; listed in SqueezeBench `SqueezeBench/Problems/Ramsey3/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.SmallRamseyNumbersWanted.graphRamsey_three_ten_le_forty_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/SmallRamseyNumbersWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html#graph-ramsey-three-ten-le-forty-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Small Ramsey numbers](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-ramsey-theory/small-ramsey-numbers)
