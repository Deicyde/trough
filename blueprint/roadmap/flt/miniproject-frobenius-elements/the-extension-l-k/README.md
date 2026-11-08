# The extension $L/K$.

Let $L^{D_Q}$ denote the fixed field of the action $D_Q$ on $L$. Our strategy for proving surjectivity of $D_Q \to \operatorname{Aut}(L/K)$ will be to write this map as the composition $D_Q \to \operatorname{Aut}(L/L^{D_Q}) \to \operatorname{Aut}(L/K)$.

The surjectivity of the first map is a general fact of Galois theory.

- [FixedPoints.toAlgAut_surjective](fixedpoints-toalgaut-surjective.md)

For surjectivity of the second map, we need to know that every element of $L^{D_Q}$ is fixed by $\operatorname{Aut}(L/K)$. We first show this for elements of $B/Q$ fixed by $D_Q$.

Now we upgrade this to elements of $L$ fixed by $D_Q$. The following lemma will allow us to lift the denominator from $B/Q$ to $A/P$.

- [IsAlgebraic.exists_smul_eq_mul](isalgebraic-exists-smul-eq-mul.md)

Combining this with [FixedPoints.toAlgAut_surjective](fixedpoints-toalgaut-surjective.md) finishes the proof.

*Proof of main theorem: shown with [Theorem IsFractionRing.stabilizerHom_surjective](../statement-of-the-theorem/isfractionring-stabilizerhom-surjective.md).*
