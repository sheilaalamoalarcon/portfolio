import { SVGIconProps } from "../components/SVGIcon";
import { SkillInfo, Skills, Project, List } from "../types/curriculum";

export const languages: SkillInfo[] = [
  { name: "HTML", level: 3 },
  { name: "CSS/SASS", level: 4 },
  { name: "JAVASCRIPT", level: 4 },
  { name: "GIT", level: 2 },
  { name: "AWS", level: 2 },
  { name: "PYTHON", level: 2 },
];
export const frameworks: SkillInfo[] = [
  { name: "EXPRESS JS", level: 3 },
  { name: "NODE JS", level: 2 },
  { name: "REACT JS", level: 3 },
  { name: "ANGULAR", level: 2 },
  { name: "REACT NATIVE", level: 3 },
];
export const softSkills: SkillInfo[] = [
  { name: "Reliable", level: 5 },
  { name: "Communicative", level: 4 },
  { name: "Adaptable", level: 4 },
];
export const skills: Skills = {
  hardSkills: {
    languages,
    frameworks,
  },
  softSkills,
};
export const allProjects: Project[] = [
  {
    title: "AppMyPets",
    body: "This mobile app fosters a dog-friendly community by enabling access to pet-friendly locations without breed or size discrimination. It encourages responsible pet ownership and offers behavior training for dogs, creating a welcoming environment for all canine companions.",
    stack: "React Native/Expo/Native",
    role: "Mobile developer",
  },
  {
    title: "MNNDZ L@b",
    body: "The app for IES Menéndez, available on Android and iOS, is designed to streamline class and event organization and provide updates on important activities such as exams and excursions. It facilitates better communication between teachers and parents, offering insights into student perspectives and enabling direct messaging for enhanced interaction and monitoring.",
    stack: "React Native/Expo",
    role: "Mobile developer",
  },
  {
    title: "Guanxe",
    body: "Online shopping platform in the Canary Islands, offering a diverse range of products with free shipping. It includes categories like shoes, clothing, baby items, health products, electronics, and more, catering to varied customer needs and ensuring a convenient shopping experience.",
    stack: "React Native/Expo/Native",
    role: "Mobile developer",
  },
];
export const workExperienceList: List = {
  title: "Work Experience",
  body: [
    "Sociedad de Promoción Económica de Gran Canaria - Las Palmas de Gran Canaria, 10/2022 - 04/2023",
    "SQUAADS - Las Palmas de Gran Canaria, 03/2023 - 12/2023",
  ],
};
export const educationList: List = {
  title: "Education",
  body: [
    "FullStack Programming Course - Las Palmas de Gran Canaria, 128 hours",
    "Artificial Intelligence Specialist - Las Palmas de Gran Canaria, 230 hours",
  ],
};
export const idiomList: List = {
  title: "Languages",
  body: ["Spanish Native", "English Mid/Advance"],
};
export const aboutMe: string =
  "I am a 24-year-old creative individual from Gran Canaria, Spain. Known for my quick learning abilities and constant availability, I have a passion for travel and cultural exploration. Fluent in Spanish and English, I also possess basic skills in Italian and am keen on improving my German. My diverse language skills and adaptability make me a valuable asset in global and multicultural settings";
export const menuIcon: SVGIconProps = {
  width: 20,
  height: 12,
  viewBox: "0 0 20 12",
  path: "M0 1H20M0 6H20M0 11H20",
};

export const envelopeIcon: SVGIconProps = {
  width: 29,
  height: 20,
  viewBox: "0 0 29 20",
  path: "M28.35 17.5V2.5C28.35 1.11667 27.2333 0 25.85 0H2.5C1.11667 0 0 1.11667 0 2.5V17.5C0 18.8833 1.11667 20 2.5 20H25.85C27.2333 20 28.35 18.8833 28.35 17.5ZM26.1667 2.31667C26.7167 2.86667 26.4167 3.43333 26.1167 3.71667L19.35 9.91667L25.85 16.6833C26.05 16.9167 26.1833 17.2833 25.95 17.5333C25.7333 17.8 25.2333 17.7833 25.0167 17.6167L17.7333 11.4L14.1667 14.65L10.6167 11.4L3.33333 17.6167C3.11667 17.7833 2.61667 17.8 2.4 17.5333C2.16667 17.2833 2.3 16.9167 2.5 16.6833L9 9.91667L2.23333 3.71667C1.93333 3.43333 1.63333 2.86667 2.18333 2.31667C2.73333 1.76667 3.3 2.03333 3.76667 2.43333L14.1667 10.8333L24.5833 2.43333C25.05 2.03333 25.6167 1.76667 26.1667 2.31667Z",
};

export const linkedinIcon: SVGIconProps = {
  width: 20,
  height: 20,
  viewBox: "0 0 20 20",
  path: "M17.7778 0C18.3671 0 18.9324 0.234126 19.3491 0.650874C19.7659 1.06762 20 1.63285 20 2.22222V17.7778C20 18.3671 19.7659 18.9324 19.3491 19.3491C18.9324 19.7659 18.3671 20 17.7778 20H2.22222C1.63285 20 1.06762 19.7659 0.650874 19.3491C0.234126 18.9324 0 18.3671 0 17.7778V2.22222C0 1.63285 0.234126 1.06762 0.650874 0.650874C1.06762 0.234126 1.63285 0 2.22222 0H17.7778ZM17.2222 17.2222V11.3333C17.2222 10.3727 16.8406 9.45133 16.1613 8.77204C15.482 8.09274 14.5607 7.71111 13.6 7.71111C12.6556 7.71111 11.5556 8.28889 11.0222 9.15556V7.92222H7.92222V17.2222H11.0222V11.7444C11.0222 10.8889 11.7111 10.1889 12.5667 10.1889C12.9792 10.1889 13.3749 10.3528 13.6666 10.6445C13.9583 10.9362 14.1222 11.3319 14.1222 11.7444V17.2222H17.2222ZM4.31111 6.17778C4.80618 6.17778 5.28098 5.98111 5.63104 5.63104C5.98111 5.28098 6.17778 4.80618 6.17778 4.31111C6.17778 3.27778 5.34444 2.43333 4.31111 2.43333C3.81309 2.43333 3.33547 2.63117 2.98332 2.98332C2.63117 3.33547 2.43333 3.81309 2.43333 4.31111C2.43333 5.34444 3.27778 6.17778 4.31111 6.17778ZM5.85556 17.2222V7.92222H2.77778V17.2222H5.85556Z",
};
export const artstationIcon: SVGIconProps = {
  width: 23,
  height: 20,
  viewBox: "0 0 23 20",
  path: "M0 15.419L1.91933 18.7378H1.92027C2.11151 19.1172 2.40433 19.4361 2.7661 19.659C3.12788 19.8818 3.54442 19.9999 3.96932 20H16.7115L14.0678 15.419H0ZM22.7251 15.4427C22.7251 14.9844 22.5897 14.5573 22.3577 14.1985L14.8925 1.22053C14.6972 0.852013 14.4052 0.54367 14.0479 0.328628C13.6906 0.113587 13.2814 -2.46158e-05 12.8643 4.0005e-09H8.91866L20.4507 19.9801L22.2687 16.8317C22.6266 16.2286 22.7251 15.9616 22.7251 15.4427ZM12.1873 12.1646L7.03342 3.23738L1.87861 12.1646H12.1873Z",
};
