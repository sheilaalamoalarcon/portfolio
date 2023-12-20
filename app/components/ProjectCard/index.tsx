import { Project } from "../../types/curriculum";
import styles from "./ProjectCard.module.css";

function ProjectCard({ title, body, stack, role, webURL }: Project) {
  return (
    <section className={styles.sectionBody}>
      <a href={webURL}>
        <h4>{title}</h4>
      </a>
      <p>{body}</p>
      <div className={styles.rowWrap}>
        <h5>Technologies</h5>
        <p>{stack}</p>
      </div>
      <div className={styles.rowWrap}>
        <h5>Role</h5>
        <p>{role}</p>
      </div>
    </section>
  );
}
export default ProjectCard;
