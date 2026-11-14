# Proof of Theorem g

Our proof of the Theorem [g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/cohn-elkies.tex#L44) relies on the following two inequalities for modular objects.

- [ineqA](prop-ineqa.md)
- [ineqB](prop-ineqb.md)

Here we formalize the proof of the inequalities by Lee (Lee). First, we can rewrite the inequality in [ineqA](prop-ineqa.md) as follows.

- [FG-definition](def-fg-definition.md)
- [F-G-phi-psi-identities](lemma-f-g-phi-psi-identities.md)

Now, the first inequality [Lemma ineqABnew-equiv](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L50) follows from the positivity of each $F(it)$ and $G(it)$.

- [F-G-pos](lemma-f-g-pos.md)
- [ineqAnew](cor-ineqanew.md)

To prove the second inequality [Lemma ineqABnew-equiv](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L50), we need some identities satisfied by $F$ and $G$.

- [FG-de](lemma-fg-de.md)
- [MLDE-pos](cor-mlde-pos.md)

The second inequality [Lemma ineqABnew-equiv](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L50) follows from the following two observations. Since $G(it) > 0$ for all $t > 0$, we can define the quotient

$$
Q(t) := \frac{F(it)}{G(it)}\qquad\text{(13)}
$$

as a function on $(0, \infty)$.

- [Qlim](lemma-qlim.md)
- [log-der-inf](lemma-log-der-inf.md)
- [Qdec](prop-qdec.md)
- [ineqBnew](cor-ineqbnew.md)

Finally, we are ready to prove Theorem [g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/cohn-elkies.tex#L44).

- [g1](thm-g1.md)

- J. Bruinier, *Borcherds products on O(2,l) and Chern classes of Heegner divisors*, Springer Lecture Notes in Mathematics 1780 (2002)
- H. Cohn, N. Elkies, *New upper bounds on sphere packings I*, Annals of Math. 157 (2003) pp. 689–714.
- F. Diamond, J. Shurman, *A First Course in Modular Forms*, Springer New York, 2005.
- D. Hejhal, *The Selberg trace formula for $\mathrm{PSL}(2, \mathbb{R})$*, Springer Lecture Notes in Mathematics 1001 (1983)
- W. Kohnen, *A Very Simple Proof of the $q$-Product Expansion of the $\Delta$-Function*, The Ramanujan Journal 10 (2005): 71-73.
- S. Lee, *Algebraic proof of modular form inequalities for optimal sphere packings*, arXiv preprint arXiv:2406.14659 (2024).
- D. Mumford, *Tata Lectures on Theta I*, Birkhäuser, 1983.
- H. Petersson, *Ueber die Entwicklungskoeffizienten der automorphen Formen*, Acta Mathematica, Bd. 58 (1932), pp. 169–215.
- H. Rademacher and H. S. Zuckerman, *On the Fourier coefficients of certain modular forms of positive dimension*, Annals of Math. (2) 39 (1938), pp. 433–462.
- J. Serre, *A Course in Arithmetic*, Springer New York, 1973.
- Maryna S. Viazovska, *The sphere packing problem in dimension 8*, Pages 991–1015 from Volume 185 (2017), Issue 3.
- D. Zagier, *Elliptic Modular Forms and Their Applications*, In: The 1-2-3 of Modular Forms, (K. Ranestad, ed.) Norway, Springer Universitext, 2008.

Ecole Polytechnique Federale de Lausanne 1015 Lausanne Switzerland *Email address: maryna.viazovska@epfl.ch*
